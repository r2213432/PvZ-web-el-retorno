import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PlantsService {

  constructor() { }

  getPlants() {
    const url: string = '${this.baseUrl}/plants'
    
  }
}
