import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ButCounter } from './but-counter';

describe('ButCounter', () => {
  let component: ButCounter;
  let fixture: ComponentFixture<ButCounter>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ButCounter]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ButCounter);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
