import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-listareservas',
  templateUrl: './listareservas.component.html',
  styleUrls: ['./listareservas.component.css'],
})
export class ListareservasComponent implements OnInit {
  reservas: any;

  constructor(private auth: AuthService) {}

  ngOnInit(): void {
    this.auth.verMisReservas().subscribe((resp) => {
      console.log(resp);
      this.reservas = resp;
    });
  }

  precioTotal(detalles: any[]): number {
    //console.log(detalles.fecha_inicio)
    //console.log(detalles.fecha_fin)
    var inicio:String
    var fin:String

    detalles.map((dat:any) => {
      //inicio=dat.fecha_inicio;
      //fin=dat.fecha_fin;

    })
//    console.log(inicio)
    return detalles.map(det => det.precio_unitario).reduce((prev, next) => prev + next);
  }
  cantidadDias(datalles:any):number{
    var inicio =new Date( datalles.fecha_inicio ).getTime();
    var fin = new Date(datalles.fecha_fin).getTime();

    var diff = fin - inicio

    return ((diff+(1000*60*60*24))/(1000*60*60*24));
  }
}
