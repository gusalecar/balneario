import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { NgForm, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { connectableObservableDescriptor } from 'rxjs/internal/observable/ConnectableObservable';
import { switchAll } from 'rxjs/operators';
import { UsuarioModel } from '../../models/usuario.model';

import { AuthService } from '../../services/auth.service';
import Swal from 'sweetalert2';



@Component({
  selector: 'app-reserva',
  templateUrl: './reserva.component.html',
  styleUrls: ['./reserva.component.css'],
})
export class ReservaComponent implements OnInit {
  mostrarCov19: boolean = true;
  fechaInicio: string;
  fechaFin: string;
  submit:boolean;
  constructor(private router: Router) {
    this.fechaInicio=''
    this.fechaFin=''

  }
  ngOnInit(): void {
    this.submit=false
  }
  irCroquis(formulario:NgForm) {
    this.submit=true;
    if (this.fechaInicio == '' || this.fechaFin =='') {
      return;
    }
    else{
    //this.router.navigate(['/croquis', this.fechaInicio, this.fechaFin])
    }
  }

}
