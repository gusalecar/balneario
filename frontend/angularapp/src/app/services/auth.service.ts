import { Injectable } from '@angular/core';
import {HttpClient } from '@angular/common/http'
import { UsuarioModel } from '../models/usuario.model';
import { parseSelectorToR3Selector } from '@angular/compiler/src/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
private url = 'http://localhost:8000/';
//this.http.post(http://localhost:8000/api/auth/register,username:test,email:test@test.com,password:pass)




  constructor(private http: HttpClient) { }

nuevoUsuario(usuario:UsuarioModel){
 const authData = {
   usuername: usuario.usuario,
   email: usuario.mail,
   password: usuario.password
 }
}
autenticarUsuario(usuario:UsuarioModel){

}
logout(){

}
}
