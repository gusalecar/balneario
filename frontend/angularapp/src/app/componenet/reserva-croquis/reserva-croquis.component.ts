import { Component, OnInit } from '@angular/core';
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

  constructor(private auth:AuthService,
    private router:Router) { }

  ngOnInit(): void {

  }

comprar(){
if(this.auth.estaAutenticado()){
  console.log('envia formulario');
  this.router.navigateByUrl('pago');
}
else{
  Swal.fire({title:'No puede seguir',
            text:'Necesita estar registrado para seguir con el proceso de reserva',
            icon:'question'
          })
}
}
}
