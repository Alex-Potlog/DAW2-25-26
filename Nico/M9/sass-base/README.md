# Sass Project

This project is a Sass-based styling framework designed to provide a modular and maintainable approach to styling web applications. It utilizes a structured file organization to separate concerns and enhance reusability.

## Project Structure

The project is organized into several directories, each serving a specific purpose:

- **src/sass/abstracts**: Contains Sass functions, mixins, and variables that can be reused throughout the project.
  - `_functions.scss`: Sass functions for styling calculations.
  - `_mixins.scss`: Reusable styles and patterns.
  - `_variables.scss`: Variable definitions for colors, fonts, and design tokens.

- **src/sass/base**: Holds the base styles for the project.
  - `_base.scss`: Default styles for elements.
  - `_reset.scss`: Resets default browser styles.
  - `_typography.scss`: Typography styles including font sizes and families.

- **src/sass/components**: Contains styles for specific UI components.
  - `_buttons.scss`: Styles for button components.
  - `_cards.scss`: Styles for card components.

- **src/sass/layout**: Defines layout-related styles.
  - `_footer.scss`: Styles for the footer layout.
  - `_grid.scss`: Grid system styles.
  - `_header.scss`: Styles for the header layout.
  - `_navigation.scss`: Styles for navigation elements.

- **src/sass/pages**: Styles specific to individual pages.
  - `_home.scss`: Styles for the home page.
  - `_about.scss`: Styles for the about page.

- **src/sass/themes**: Contains theme-specific styles.
  - `_dark.scss`: Styles for a dark theme.
  - `_light.scss`: Styles for a light theme.

- **src/sass/vendors**: Includes third-party styles.
  - `_bootstrap.scss`: Imports Bootstrap styles.

- **src/sass/main.scss**: The main Sass file that imports all other Sass files, compiling them into a single CSS file.

## Installation

To get started with this project, clone the repository and install the dependencies:

```bash
npm install
```

## Usage

To compile the Sass files into CSS, run the following command:

```bash
npm run build
```

This will generate the final CSS file from the Sass source files.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.