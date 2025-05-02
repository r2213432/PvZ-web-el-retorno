import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PvzAComponent } from './pvz-a.component';

describe('PvzAComponent', () => {
  let component: PvzAComponent;
  let fixture: ComponentFixture<PvzAComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PvzAComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PvzAComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
