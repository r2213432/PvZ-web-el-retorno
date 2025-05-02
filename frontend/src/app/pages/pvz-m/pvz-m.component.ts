import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-pvz-m',
  standalone: true, 
  imports: [CommonModule, RouterLink],
  templateUrl: './pvz-m.component.html',
  styleUrls: ['./pvz-m.component.css']
})
export class PvzMComponent {

    ngOnInit() {
        document.body.style.backgroundColor = '#E0E2DC'; 
      }

    src: string = "https://i0.wp.com/www.pcmrace.com/wp-content/uploads/2017/11/plants-vs-zombies-game-of-the-year-edition_pdp_3840x2160_en_WW.jpg?fit=1920%2C1080&amp;ssl=1";
    contador: number = 1;
  
    siguienteImagen() {
      if (this.contador === 1) {
        this.src = "https://i.imgur.com/jQhHK48.png";
        this.contador = 2;
      } else if (this.contador === 2) {
        this.src = "https://i.imgur.com/CdjE0xt.png";
        this.contador = 3;
      } else if (this.contador === 3) {
        this.src = "https://i0.wp.com/www.pcmrace.com/wp-content/uploads/2017/11/plants-vs-zombies-game-of-the-year-edition_pdp_3840x2160_en_WW.jpg?fit=1920%2C1080&amp;ssl=1";
        this.contador = 1;
      }
    }
  
    anteriorImagen() {
      if (this.contador === 1) {
        this.src = "https://i.imgur.com/CdjE0xt.png";
        this.contador = 3;
      } else if (this.contador === 2) {
        this.src = "https://i0.wp.com/www.pcmrace.com/wp-content/uploads/2017/11/plants-vs-zombies-game-of-the-year-edition_pdp_3840x2160_en_WW.jpg?fit=1920%2C1080&amp;ssl=1";
        this.contador = 1;
      } else if (this.contador === 3) {
        this.src = "https://i.imgur.com/jQhHK48.png";
        this.contador = 2;
      }
    }
  }