import { TestBed } from '@angular/core/testing';

import { PlantsService } from './plants.service';

describe('PlantsService', () => {
  let service: PlantsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PlantsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
