import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import Swal from 'sweetalert2';
declare var jQuery:any;
declare var $:any;

@Component({
  selector: 'app-reserva-croquis',
  templateUrl: './reserva-croquis.component.html',
  styleUrls: ['./reserva-croquis.component.css']
})
export class ReservaCroquisComponent implements OnInit {
ctrFlechasSombrillas: boolean;
ctrFlechasCarpas: boolean;


  constructor(private auth:AuthService,
    private router:Router) {

     }

  ngOnInit(): void {
    this.ctrFlechasCarpas=true;
    this.ctrFlechasSombrillas=true;
  }

comprar(){
if(this.auth.estaAutenticado()){
  console.log('envia formulario');
  Swal.fire({
    title: 'Error',
    text:'No se pudo concretar la reserva, "error especifico"',
    icon:'error'
  })
  //this.router.navigateByUrl('pago');
}
else{
  Swal.fire({title:'No puede seguir',
            text:'Necesita estar registrado para realizar la reserva',
            icon:'info'
          })
}
}

botonSombrillas(){
  this.ctrFlechasSombrillas=!this.ctrFlechasSombrillas;
}

botonCarpas(){
  this.ctrFlechasCarpas=!this.ctrFlechasCarpas;
}
}
