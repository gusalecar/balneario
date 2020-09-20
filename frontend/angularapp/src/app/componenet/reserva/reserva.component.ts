import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-reserva',
  templateUrl: './reserva.component.html',
  styleUrls: ['./reserva.component.css']
})
export class ReservaComponent implements OnInit {
mostrarCov19:boolean=true;
  constructor() { }

  ngOnInit(): void {
  }

mostrarOcultarCov19(){
  
  if(this.mostrarCov19=true){
this.mostrarCov19=false;
  }
  if(this.mostrarCov19=false){
    this.mostrarCov19=true;
    
      }
}
}
