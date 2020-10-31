import { Component, OnInit } from '@angular/core';
import { NgForm, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { connectableObservableDescriptor } from 'rxjs/internal/observable/ConnectableObservable';
import { switchAll } from 'rxjs/operators';
import { UsuarioModel } from '../../models/usuario.model';

import { AuthService } from '../../services/auth.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
})
export class NavbarComponent implements OnInit {
  usuario: UsuarioModel;
  passwordConfirm: string;
  usuariologin: UsuarioModel;
  logueado: boolean;
  user: string;
  passDiferente: boolean;

  constructor(private auth: AuthService) {
    if (localStorage.getItem('token')) {
      this.logueado = true;
    } else {
      this.logueado = false;
    }
    if (localStorage.getItem('usuario')) {
      this.user = localStorage.getItem('usuario');
    }
  }

  ngOnInit(): void {
    this.usuario = new UsuarioModel();
    this.usuariologin = new UsuarioModel();
  }

  onSubmit(formulario: NgForm) {
    if (this.usuario.password != this.passwordConfirm) {
      this.passDiferente = true;
      return;
    }
    else {
      this.passDiferente = false;
    }
    if (formulario.invalid) {
      return;
    }
    Swal.fire({
      icon: 'info',
      allowOutsideClick: false,
      text: 'Espere por favor...',
    });
    Swal.showLoading();
    this.auth.nuevoUsuario(this.usuario).subscribe(
      (respusta) => {
        console.log(respusta);
        Swal.close();
        Swal.fire({
          icon: 'success',
          title: 'El usuario se creo correctamente',
        });
      },
      (error) => {
        console.log(error);
        if (error.error.email == 'This field must be unique.') {
          Swal.close();
          Swal.fire({ icon: 'error', text: 'E-MAIL ya registrado' });
        }
        if (
          error.error.username == 'A user with that username already exists.'
        ) {
          Swal.fire({ icon: 'error', text: 'Usuario Existente' });
        }
        if (
          error.message ==
          'Http failure response for http://localhost:8000/api/auth/register: 0 Unknown Error'
        ) {
          Swal.close();
          Swal.fire({
            icon: 'error',
            text: 'Error de comunicacion con el servidor',
          });
        }
      }
    );
  }

  onSubmitLogin(formulario: NgForm) {
    if (formulario.invalid) {
      return;
    }
    Swal.fire({
      icon: 'info',
      allowOutsideClick: false,
      text: 'Espere por favor...',
    });
    Swal.showLoading();
    this.auth.autenticarUsuario(this.usuariologin).subscribe(
      (respuesta) => {
        Swal.close();
        this.logueado = true;
        Swal.fire({ icon: 'success', title: '¡Bienvenido!' });
      },
      (error) => {
        console.log(error);
        if (
          error.message ==
          'Http failure response for http://localhost:8000/api/auth/token: 0 Unknown Error'
        ) {
          Swal.fire({
            icon: 'error',
            text: 'Error de comunicacion con el servidor',
          });
        } else {
          Swal.fire({
            icon: 'error',
            text:
              'Error de autenticacion, usuario inexistente o contraseña erronea',
          });
        }
      }
    );
  }

  logout() {
    this.auth.logout();
    this.logueado = false;
  }
  autenticado(){
    this.auth.estaAutenticado();

  }

}
