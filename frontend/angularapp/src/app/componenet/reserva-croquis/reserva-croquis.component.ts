import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import Swal from 'sweetalert2';

import { DetallesModel } from '../../models/detalles.model';
import { ItemModel } from '../../models/Item.model'

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
precioCarpa= 21000;
precioSombrilla= 14000;
carpa:number=0;
carpas:number[]=[];
sombrilla:number=0;
sombrillas:number[]=[];
total:number=0;
reservable:DetallesModel []=[{
 estado:true,
  item: {
    numero: 1,
    tipo: "carpa"
  }
},
{
estado:false,
  item: {
    numero: 2,
    tipo: "carpa"
  }
},
{
estado:true,
  item: {
    numero: 3,
    tipo: "carpa"
  }
},
{
estado: false,
  item: {
    numero: 4,
    tipo: "carpa"
  }
},
{
estado:true,
  item: {
    numero: 5,
    tipo: "carpa"
  }
},{
estado:true,
  item: {
    numero: 6,
    tipo: "carpa"
  }
},
{
estado: true,
  item: {
    numero: 7,
    tipo: "carpa"
  }
}];

  constructor(private auth:AuthService,
    private router:Router) {

console.log(this.reservable.length);
     }

  ngOnInit(): void {
    this.ctrFlechasCarpas=true;
    this.ctrFlechasSombrillas=true;
    //this.reservableReservado();
    this.botonReservar();

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

seleccionarCarpa(id:string){

}

reservableReservado(){
  for (let posicion of this.reservable){
    if(posicion.item.tipo=='carpa'){
      if(posicion.estado){
        (<HTMLInputElement> document.getElementById(`c${posicion.item.numero}`)).disabled=true;
        document.getElementById(`c${posicion.item.numero}`).style.opacity='1';
      }
    }
    if(posicion.item.tipo=='sombrilla'){
      if(posicion.estado){
        (<HTMLInputElement> document.getElementById(`c${posicion.item.numero}`)).disabled=true;
        document.getElementById(`c${posicion.item.numero}`).style.opacity='1';
      }
    }
  }
}
reservableSeleccionar(id:string, tipo:string, numero:number){
  if(tipo=='carpa'){
    if(this.carpaSeleccionada(numero)){
      document.getElementById(id).style.background='blue';
      this.carpas.push(numero);
      this.carpa=this.carpas.length;
      this.calcularTotal();
      console.log(this.carpas);
    }
    else{
      document.getElementById(id).style.background='gray'
      this.carpas=this.eliminarNumero(numero,this.carpas);
      console.log(this.carpas);
      this.calcularTotal();
      this.carpa=this.carpas.length;
    }
  }
  if(tipo=='sombrilla'){
    if(this.sombrillaSeleccionada(numero)){
      document.getElementById(id).style.background='blue';
      this.sombrillas.push(numero);
      this.sombrilla=this.sombrillas.length;
      this.calcularTotal();
    }
    else{
      document.getElementById(id).style.background='gray'
      this.sombrillas=this.eliminarNumero(numero,this.sombrillas);
      console.log(this.sombrillas);
      this.calcularTotal();
      this.sombrilla=this.sombrillas.length;
    }
  }
}
eliminarNumero(numero:number, arreglo:number[]):number[]{
  var localArray:number[]=[];
  for (let value of arreglo){
    if(value!=numero){
      localArray.push(value);
    }
  }
  return localArray;
}
carpaSeleccionada(numero:number):boolean{
    for(let value of this.carpas){
      if(value==numero){
        return false;
      }
    }
  return true;
}
sombrillaSeleccionada(numero:number):boolean{
  for(let value of this.sombrillas){
    if(value==numero){
      return false;
    }
  }
return true;
}
calcularTotal(){
  this.total=this.precioCarpa*this.carpas.length+this.precioSombrilla*this.sombrillas.length;
  this.botonReservar();
}


botonReservar(){

  if(this.carpas.length > 0 || this.sombrillas.length > 0){
    (<HTMLInputElement> document.getElementById(`botonReservar`)).disabled=false;
  }
  else{
    (<HTMLInputElement> document.getElementById(`botonReservar`)).disabled=false;
  }
}
}
