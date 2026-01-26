-- ============================================
-- ESQUEMA BASE DE DADES - PLATAFORMA DE CURSOS
-- PostgreSQL 16
-- ============================================

-- Crear extensions necessàries
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";  -- Per generar UUIDs
CREATE EXTENSION IF NOT EXISTS "pg_trgm";     -- Per cerca fuzzy
CREATE EXTENSION IF NOT EXISTS "pgcrypto";    -- Per encriptació

-- ============================================
-- 1. TAULA: USERS (Usuaris)
-- ============================================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'student' CHECK (role IN ('admin', 'instructor', 'student')),
    bio TEXT,
    profile_picture_url VARCHAR(500),
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    last_login_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_is_active ON users(is_active);

COMMENT ON TABLE users IS 'Taula principal d''usuaris (admins, instructors, estudiants)';
COMMENT ON COLUMN users.is_verified IS 'Indica si l''email ha estat verificat';

-- ============================================
-- 2. TAULA: CATEGORIES (Categories de cursos)
-- ============================================
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    slug VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    icon_url VARCHAR(500),
    parent_category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_categories_slug ON categories(slug);
CREATE INDEX idx_categories_parent ON categories(parent_category_id);

COMMENT ON TABLE categories IS 'Categories i subcategories de cursos (jerarquia)';

-- ============================================
-- 3. TAULA: COURSES (Cursos)
-- ============================================
CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    short_description VARCHAR(500),
    thumbnail_url VARCHAR(500),
    promo_video_url VARCHAR(500),
    category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL,
    level VARCHAR(20) CHECK (level IN ('beginner', 'intermediate', 'advanced', 'all_levels')),
    language VARCHAR(10) DEFAULT 'es',
    
    -- Preus i model de negoci
    is_free BOOLEAN DEFAULT FALSE,
    base_price DECIMAL(10,2),
    discounted_price DECIMAL(10,2),
    is_subscription_only BOOLEAN DEFAULT FALSE,  -- Si només accessible amb subscripció
    
    -- Control de publicació
    status VARCHAR(20) DEFAULT 'draft' CHECK (status IN ('draft', 'pending_review', 'published', 'archived')),
    is_published BOOLEAN DEFAULT FALSE,
    published_at TIMESTAMP,
    
    -- Metadades
    total_duration_minutes INTEGER DEFAULT 0,  -- Durada total en minuts
    total_lessons INTEGER DEFAULT 0,
    total_students INTEGER DEFAULT 0,
    average_rating DECIMAL(3,2) DEFAULT 0.00,
    total_reviews INTEGER DEFAULT 0,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_courses_slug ON courses(slug);
CREATE INDEX idx_courses_category ON courses(category_id);
CREATE INDEX idx_courses_status ON courses(status);
CREATE INDEX idx_courses_is_published ON courses(is_published);
CREATE INDEX idx_courses_average_rating ON courses(average_rating);
CREATE INDEX idx_courses_created_at ON courses(created_at DESC);

COMMENT ON TABLE courses IS 'Taula principal de cursos';
COMMENT ON COLUMN courses.status IS 'draft=esborrany, pending_review=pendent verificació, published=publicat, archived=arxivat';

-- ============================================
-- 4. TAULA: COURSE_INSTRUCTORS (Relació cursos-instructors)
-- ============================================
CREATE TABLE course_instructors (
    id SERIAL PRIMARY KEY,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    instructor_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role VARCHAR(20) DEFAULT 'co_instructor' CHECK (role IN ('main_instructor', 'co_instructor')),
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(course_id, instructor_id)
);

CREATE INDEX idx_course_instructors_course ON course_instructors(course_id);
CREATE INDEX idx_course_instructors_instructor ON course_instructors(instructor_id);

COMMENT ON TABLE course_instructors IS 'Relació many-to-many entre cursos i instructors';

-- ============================================
-- 5. TAULA: COURSE_PREREQUISITES (Prerequisits)
-- ============================================
CREATE TABLE course_prerequisites (
    id SERIAL PRIMARY KEY,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    prerequisite_course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    is_required BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(course_id, prerequisite_course_id),
    CHECK (course_id != prerequisite_course_id)  -- Un curs no pot ser prerequisit de si mateix
);

CREATE INDEX idx_prerequisites_course ON course_prerequisites(course_id);
CREATE INDEX idx_prerequisites_prereq_course ON course_prerequisites(prerequisite_course_id);

COMMENT ON TABLE course_prerequisites IS 'Cursos que són prerequisit d''altres cursos';

-- ============================================
-- 6. TAULA: SECTIONS (Seccions dins dels cursos)
-- ============================================
CREATE TABLE sections (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(course_id, order_index)
);

CREATE INDEX idx_sections_course ON sections(course_id);
CREATE INDEX idx_sections_order ON sections(course_id, order_index);

COMMENT ON TABLE sections IS 'Seccions que agrupen lliçons dins d''un curs';

-- ============================================
-- 7. TAULA: LESSONS (Lliçons)
-- ============================================
CREATE TABLE lessons (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    section_id UUID NOT NULL REFERENCES sections(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    content_type VARCHAR(20) NOT NULL CHECK (content_type IN ('video', 'article', 'quiz', 'assignment', 'resource')),
    
    -- URL del contingut (vídeo, PDF, etc.)
    content_url VARCHAR(500),
    
    -- Durada (en minuts per vídeos)
    duration_minutes INTEGER,
    
    -- Per articles de text
    article_content TEXT,
    
    -- Control d'accés
    is_preview BOOLEAN DEFAULT FALSE,  -- Si es pot veure sense estar inscrit
    is_free BOOLEAN DEFAULT FALSE,
    
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(section_id, order_index)
);

CREATE INDEX idx_lessons_section ON lessons(section_id);
CREATE INDEX idx_lessons_content_type ON lessons(content_type);
CREATE INDEX idx_lessons_order ON lessons(section_id, order_index);

COMMENT ON TABLE lessons IS 'Lliçons individuals dins de cada secció';

-- ============================================
-- 8. TAULA: LESSON_RESOURCES (Recursos descarregables)
-- ============================================
CREATE TABLE lesson_resources (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    lesson_id UUID NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    file_url VARCHAR(500) NOT NULL,
    file_type VARCHAR(50),  -- pdf, zip, docx, etc.
    file_size_mb DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_resources_lesson ON lesson_resources(lesson_id);

COMMENT ON TABLE lesson_resources IS 'Arxius descarregables associats a lliçons';

-- ============================================
-- 9. TAULA: QUIZZES (Qüestionaris)
-- ============================================
CREATE TABLE quizzes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    lesson_id UUID NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    passing_score INTEGER NOT NULL DEFAULT 70,  -- Percentatge mínim per aprovar
    max_attempts INTEGER,  -- NULL = intents il·limitats
    time_limit_minutes INTEGER,  -- NULL = sense límit de temps
    is_randomized BOOLEAN DEFAULT FALSE,  -- Barrejar preguntes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_quizzes_lesson ON quizzes(lesson_id);

COMMENT ON TABLE quizzes IS 'Qüestionaris associats a lliçons';

-- ============================================
-- 10. TAULA: QUIZ_QUESTIONS (Preguntes dels qüestionaris)
-- ============================================
CREATE TABLE quiz_questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    quiz_id UUID NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE,
    question_type VARCHAR(20) NOT NULL CHECK (question_type IN ('multiple_choice', 'open_ended')),
    question_text TEXT NOT NULL,
    points INTEGER DEFAULT 1,
    order_index INTEGER NOT NULL,
    
    -- Per open-ended (pregunta oberta)
    max_words INTEGER,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(quiz_id, order_index)
);

CREATE INDEX idx_quiz_questions_quiz ON quiz_questions(quiz_id);

COMMENT ON TABLE quiz_questions IS 'Preguntes individuals de cada qüestionari';

-- ============================================
-- 11. TAULA: QUIZ_QUESTION_OPTIONS (Opcions resposta múltiple)
-- ============================================
CREATE TABLE quiz_question_options (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    question_id UUID NOT NULL REFERENCES quiz_questions(id) ON DELETE CASCADE,
    option_text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT FALSE,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(question_id, order_index)
);

CREATE INDEX idx_question_options_question ON quiz_question_options(question_id);

COMMENT ON TABLE quiz_question_options IS 'Opcions per preguntes de resposta múltiple';

-- ============================================
-- 12. TAULA: ASSIGNMENTS (Tasques/Projectes)
-- ============================================
CREATE TABLE assignments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    lesson_id UUID NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    instructions TEXT NOT NULL,
    max_file_size_mb INTEGER DEFAULT 10,
    allowed_file_types VARCHAR(255),  -- Ex: 'pdf,zip,docx'
    max_attempts INTEGER,
    deadline_days INTEGER,  -- Dies des de la inscripció
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_assignments_lesson ON assignments(lesson_id);

COMMENT ON TABLE assignments IS 'Tasques amb entrega de fitxers';

-- ============================================
-- 13. TAULA: ENROLLMENTS (Inscripcions a cursos)
-- ============================================
CREATE TABLE enrollments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    
    -- Tipus d'accés
    access_type VARCHAR(20) NOT NULL CHECK (access_type IN ('free', 'paid', 'subscription', 'coupon')),
    
    -- Progrés
    progress_percentage INTEGER DEFAULT 0 CHECK (progress_percentage >= 0 AND progress_percentage <= 100),
    completed_at TIMESTAMP,
    last_accessed_at TIMESTAMP,
    
    -- Per subscripcions
    subscription_expires_at TIMESTAMP,
    
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, course_id)
);

CREATE INDEX idx_enrollments_user ON enrollments(user_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);
CREATE INDEX idx_enrollments_completed ON enrollments(completed_at);
CREATE INDEX idx_enrollments_access_type ON enrollments(access_type);

COMMENT ON TABLE enrollments IS 'Inscripcions d''estudiants a cursos';

-- ============================================
-- 14. TAULA: LESSON_PROGRESS (Progrés per lliçó)
-- ============================================
CREATE TABLE lesson_progress (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    enrollment_id UUID NOT NULL REFERENCES enrollments(id) ON DELETE CASCADE,
    lesson_id UUID NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
    is_completed BOOLEAN DEFAULT FALSE,
    last_position_seconds INTEGER DEFAULT 0,  -- Per vídeos: segon on es va quedar
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(enrollment_id, lesson_id)
);

CREATE INDEX idx_lesson_progress_enrollment ON lesson_progress(enrollment_id);
CREATE INDEX idx_lesson_progress_lesson ON lesson_progress(lesson_id);

COMMENT ON TABLE lesson_progress IS 'Progrés individual per cada lliçó';

-- ============================================
-- 15. TAULA: QUIZ_ATTEMPTS (Intents de qüestionaris)
-- ============================================
CREATE TABLE quiz_attempts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    enrollment_id UUID NOT NULL REFERENCES enrollments(id) ON DELETE CASCADE,
    quiz_id UUID NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE,
    attempt_number INTEGER NOT NULL DEFAULT 1,
    score INTEGER,  -- Punts obtinguts
    max_score INTEGER,  -- Punts totals possibles
    percentage DECIMAL(5,2),  -- Percentatge
    is_passed BOOLEAN DEFAULT FALSE,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    time_spent_minutes INTEGER,
    UNIQUE(enrollment_id, quiz_id, attempt_number)
);

CREATE INDEX idx_quiz_attempts_enrollment ON quiz_attempts(enrollment_id);
CREATE INDEX idx_quiz_attempts_quiz ON quiz_attempts(quiz_id);

COMMENT ON TABLE quiz_attempts IS 'Intents d''estudiants en qüestionaris';

-- ============================================
-- 16. TAULA: QUIZ_ANSWERS (Respostes a preguntes)
-- ============================================
CREATE TABLE quiz_answers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    attempt_id UUID NOT NULL REFERENCES quiz_attempts(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES quiz_questions(id) ON DELETE CASCADE,
    
    -- Per multiple choice
    selected_option_id UUID REFERENCES quiz_question_options(id) ON DELETE SET NULL,
    
    -- Per open-ended
    answer_text TEXT,
    
    is_correct BOOLEAN,  -- NULL si encara no s'ha corregit (open-ended)
    points_earned INTEGER DEFAULT 0,
    instructor_feedback TEXT,
    graded_at TIMESTAMP,
    graded_by UUID REFERENCES users(id) ON DELETE SET NULL,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(attempt_id, question_id)
);

CREATE INDEX idx_quiz_answers_attempt ON quiz_answers(attempt_id);
CREATE INDEX idx_quiz_answers_question ON quiz_answers(question_id);

COMMENT ON TABLE quiz_answers IS 'Respostes individuals a preguntes de qüestionaris';

-- ============================================
-- 17. TAULA: ASSIGNMENT_SUBMISSIONS (Entregues de tasques)
-- ============================================
CREATE TABLE assignment_submissions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    enrollment_id UUID NOT NULL REFERENCES enrollments(id) ON DELETE CASCADE,
    assignment_id UUID NOT NULL REFERENCES assignments(id) ON DELETE CASCADE,
    attempt_number INTEGER NOT NULL DEFAULT 1,
    file_url VARCHAR(500) NOT NULL,
    file_name VARCHAR(255),
    file_size_mb DECIMAL(10,2),
    comments TEXT,
    
    -- Avaluació
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    instructor_feedback TEXT,
    graded_at TIMESTAMP,
    graded_by UUID REFERENCES users(id) ON DELETE SET NULL,
    
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(enrollment_id, assignment_id, attempt_number)
);

CREATE INDEX idx_submissions_enrollment ON assignment_submissions(enrollment_id);
CREATE INDEX idx_submissions_assignment ON assignment_submissions(assignment_id);
CREATE INDEX idx_submissions_graded ON assignment_submissions(graded_at);

COMMENT ON TABLE assignment_submissions IS 'Entregues d''estudiants per tasques';

-- ============================================
-- 18. TAULA: CERTIFICATES (Certificats)
-- ============================================
CREATE TABLE certificates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    enrollment_id UUID NOT NULL REFERENCES enrollments(id) ON DELETE CASCADE,
    certificate_url VARCHAR(500) NOT NULL,
    verification_code VARCHAR(50) UNIQUE NOT NULL,
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(enrollment_id)
);

CREATE INDEX idx_certificates_enrollment ON certificates(enrollment_id);
CREATE INDEX idx_certificates_verification ON certificates(verification_code);

COMMENT ON TABLE certificates IS 'Certificats emesos (NO automàtics)';

-- ============================================
-- 19. TAULA: PAYMENTS (Pagaments)
-- ============================================
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    course_id UUID REFERENCES courses(id) ON DELETE SET NULL,
    
    payment_type VARCHAR(20) NOT NULL CHECK (payment_type IN ('course_purchase', 'subscription')),
    
    amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'EUR',
    
    -- Integració Stripe
    stripe_payment_id VARCHAR(255),
    stripe_customer_id VARCHAR(255),
    
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    
    payment_method VARCHAR(50),  -- card, paypal, etc.
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

CREATE INDEX idx_payments_user ON payments(user_id);
CREATE INDEX idx_payments_course ON payments(course_id);
CREATE INDEX idx_payments_status ON payments(status);
CREATE INDEX idx_payments_stripe ON payments(stripe_payment_id);

COMMENT ON TABLE payments IS 'Historial de pagaments (cursos i subscripcions)';

-- ============================================
-- 20. TAULA: SUBSCRIPTIONS (Subscripcions)
-- ============================================
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    plan_type VARCHAR(20) NOT NULL CHECK (plan_type IN ('monthly', 'annual')),
    
    stripe_subscription_id VARCHAR(255) UNIQUE,
    
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'cancelled', 'expired', 'paused')),
    
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    current_period_end TIMESTAMP NOT NULL,
    cancelled_at TIMESTAMP,
    
    UNIQUE(user_id, status)  -- Un usuari només pot tenir una subscripció activa
);

CREATE INDEX idx_subscriptions_user ON subscriptions(user_id);
CREATE INDEX idx_subscriptions_status ON subscriptions(status);
CREATE INDEX idx_subscriptions_stripe ON subscriptions(stripe_subscription_id);

COMMENT ON TABLE subscriptions IS 'Subscripcions actives dels usuaris';

-- ============================================
-- 21. TAULA: COUPONS (Cupons de descompte)
-- ============================================
CREATE TABLE coupons (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    code VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    
    discount_type VARCHAR(20) NOT NULL CHECK (discount_type IN ('percentage', 'fixed_amount')),
    discount_value DECIMAL(10,2) NOT NULL,
    
    -- Aplicable a
    course_id UUID REFERENCES courses(id) ON DELETE CASCADE,  -- NULL = tots els cursos
    
    max_uses INTEGER,  -- NULL = usos il·limitats
    current_uses INTEGER DEFAULT 0,
    
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valid_until TIMESTAMP,
    
    is_active BOOLEAN DEFAULT TRUE,
    created_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_coupons_code ON coupons(code);
CREATE INDEX idx_coupons_course ON coupons(course_id);
CREATE INDEX idx_coupons_active ON coupons(is_active);

COMMENT ON TABLE coupons IS 'Cupons de descompte per cursos';

-- ============================================
-- 22. TAULA: COUPON_USAGES (Usos de cupons)
-- ============================================
CREATE TABLE coupon_usages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    coupon_id UUID NOT NULL REFERENCES coupons(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    payment_id UUID REFERENCES payments(id) ON DELETE SET NULL,
    discount_applied DECIMAL(10,2) NOT NULL,
    used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(coupon_id, user_id)  -- Un usuari només pot usar un cupó una vegada
);

CREATE INDEX idx_coupon_usages_coupon ON coupon_usages(coupon_id);
CREATE INDEX idx_coupon_usages_user ON coupon_usages(user_id);

COMMENT ON TABLE coupon_usages IS 'Registre d''ús de cupons per usuaris';

-- ============================================
-- 23. TAULA: AFFILIATE_LINKS (Enllaços d'afiliats)
-- ============================================
CREATE TABLE affiliate_links (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    instructor_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    affiliate_code VARCHAR(50) UNIQUE NOT NULL,
    commission_percentage DECIMAL(5,2) DEFAULT 10.00,
    total_clicks INTEGER DEFAULT 0,
    total_conversions INTEGER DEFAULT 0,
    total_earnings DECIMAL(10,2) DEFAULT 0.00,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(instructor_id, course_id)
);

CREATE INDEX idx_affiliate_instructor ON affiliate_links(instructor_id);
CREATE INDEX idx_affiliate_course ON affiliate_links(course_id);
CREATE INDEX idx_affiliate_code ON affiliate_links(affiliate_code);

COMMENT ON TABLE affiliate_links IS 'Enllaços d''afiliats per instructors';

-- ============================================
-- 24. TAULA: AFFILIATE_CLICKS (Clicks en enllaços)
-- ============================================
CREATE TABLE affiliate_clicks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    affiliate_link_id UUID NOT NULL REFERENCES affiliate_links(id) ON DELETE CASCADE,
    ip_address INET,
    user_agent TEXT,
    clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_affiliate_clicks_link ON affiliate_clicks(affiliate_link_id);
CREATE INDEX idx_affiliate_clicks_date ON affiliate_clicks(clicked_at);

COMMENT ON TABLE affiliate_clicks IS 'Registre de clicks en enllaços d''afiliats';

-- ============================================
-- 25. TAULA: AFFILIATE_COMMISSIONS (Comissions d'afiliats)
-- ============================================
CREATE TABLE affiliate_commissions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    affiliate_link_id UUID NOT NULL REFERENCES affiliate_links(id) ON DELETE CASCADE,
    payment_id UUID NOT NULL REFERENCES payments(id) ON DELETE CASCADE,
    commission_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'paid')),
    paid_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_commissions_affiliate ON affiliate_commissions(affiliate_link_id);
CREATE INDEX idx_commissions_payment ON affiliate_commissions(payment_id);
CREATE INDEX idx_commissions_status ON affiliate_commissions(status);

COMMENT ON TABLE affiliate_commissions IS 'Comissions generades per afiliats';

-- ============================================
-- 26. TAULA: REVIEWS (Valoracions de cursos)
-- ============================================
CREATE TABLE reviews (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(course_id, user_id)  -- Un usuari només pot valorar un curs una vegada
);

CREATE INDEX idx_reviews_course ON reviews(course_id);
CREATE INDEX idx_reviews_user ON reviews(user_id);
CREATE INDEX idx_reviews_rating ON reviews(rating);

COMMENT ON TABLE reviews IS 'Valoracions i comentaris de cursos';

-- ============================================
-- 27. TAULA: INSTRUCTOR_RATINGS (Valoracions d'instructors)
-- ============================================
CREATE TABLE instructor_ratings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    instructor_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(instructor_id, user_id, course_id)
);

CREATE INDEX idx_instructor_ratings_instructor ON instructor_ratings(instructor_id);
CREATE INDEX idx_instructor_ratings_course ON instructor_ratings(course_id);

COMMENT ON TABLE instructor_ratings IS 'Valoracions específiques d''instructors';

-- ============================================
-- 28. TAULA: FORUMS (Fòrums de cursos)
-- ============================================
CREATE TABLE forums (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    is_archived BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(course_id)  -- Un fòrum per curs
);

CREATE INDEX idx_forums_course ON forums(course_id);
CREATE INDEX idx_forums_archived ON forums(is_archived);

COMMENT ON TABLE forums IS 'Fòrums de discussió per curs';

-- ============================================
-- 29. TAULA: FORUM_THREADS (Fils de discussió)
-- ============================================
CREATE TABLE forum_threads (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    forum_id UUID NOT NULL REFERENCES forums(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    is_pinned BOOLEAN DEFAULT FALSE,
    is_locked BOOLEAN DEFAULT FALSE,
    views_count INTEGER DEFAULT 0,
    replies_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_forum_threads_forum ON forum_threads(forum_id);
CREATE INDEX idx_forum_threads_user ON forum_threads(user_id);
CREATE INDEX idx_forum_threads_created ON forum_threads(created_at DESC);

COMMENT ON TABLE forum_threads IS 'Fils de discussió dins dels fòrums';

-- ============================================
-- 30. TAULA: FORUM_REPLIES (Respostes a fils)
-- ============================================
CREATE TABLE forum_replies (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    thread_id UUID NOT NULL REFERENCES forum_threads(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    parent_reply_id UUID REFERENCES forum_replies(id) ON DELETE CASCADE,  -- Per respostes niuades
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_forum_replies_thread ON forum_replies(thread_id);
CREATE INDEX idx_forum_replies_user ON forum_replies(user_id);
CREATE INDEX idx_forum_replies_parent ON forum_replies(parent_reply_id);
CREATE INDEX idx_forum_replies_created ON forum_replies(created_at);

COMMENT ON TABLE forum_replies IS 'Respostes a fils de discussió';

-- ============================================
-- 31. TAULA: FORUM_SUBSCRIPTIONS (Seguiment de fils)
-- ============================================
CREATE TABLE forum_subscriptions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    thread_id UUID NOT NULL REFERENCES forum_threads(id) ON DELETE CASCADE,
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, thread_id)
);

CREATE INDEX idx_forum_subs_user ON forum_subscriptions(user_id);
CREATE INDEX idx_forum_subs_thread ON forum_subscriptions(thread_id);

COMMENT ON TABLE forum_subscriptions IS 'Usuaris que segueixen fils per rebre notificacions';

-- ============================================
-- 32. TAULA: MESSAGES (Missatges privats)
-- ============================================
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v