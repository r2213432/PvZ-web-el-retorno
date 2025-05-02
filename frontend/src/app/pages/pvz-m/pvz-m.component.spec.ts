import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PvzMComponent } from './pvz-m.component';

describe('PvzMComponent', () => {
  let component: PvzMComponent;
  let fixture: ComponentFixture<PvzMComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PvzMComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PvzMComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
