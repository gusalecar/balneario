import { Injectable } from '@angular/core';
import {HttpClient } from '@angular/common/http'
import { UsuarioModel } from '../models/usuario.model';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
private url = 'http://localhost:8000/';
userToken: string;
  constructor(private http: HttpClient) { }

nuevoUsuario(usuario:UsuarioModel){
 const authData = {
   username: usuario.usuario,
   email: usuario.mail,
   password: usuario.password
 }
 return this.http.post(`${this.url}api/auth/register`, authData);
} 
autenticarUsuario(usuario:UsuarioModel){
  const authData2 = {
    username: usuario.usuario,
    password: usuario.password
  }
  return this.http.post(`${this.url}api/auth/token`, authData2).pipe(map(resp=>{
    this.guardarToken(resp['access']);
    return resp;
  } ));
}
logout(){
}
private guardarToken(idToken:string){
  this.userToken=idToken;
  localStorage.setItem('token',idToken);
}
leerToken(){
  if(localStorage.getItem('token')){
    this.userToken=localStorage.getItem('token');
  }
  else{
    this.userToken='';
  }
}

}
