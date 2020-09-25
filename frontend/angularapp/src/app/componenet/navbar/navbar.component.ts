import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { UsuarioModel} from '../../models/usuario.model'
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
usuario: UsuarioModel;
passwordConfirm: string;
usuariologin:UsuarioModel;
  constructor() { }

  ngOnInit(): void {
    this.usuario= new UsuarioModel;
    this.usuariologin= new UsuarioModel;
  }

  onSubmit(formulario: NgForm){
    console.log('formulario enviado');
    console.log(this.usuario);
    console.log(formulario); 
  }

  onSubmitLogin(formulario: NgForm){
    
    console.log('formulario enviado');
    console.log(this.usuariologin);
    console.log(formulario); 
  }
}
