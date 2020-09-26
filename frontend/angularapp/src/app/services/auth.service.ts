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
usuario:string;
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
    this.guardarUsuario(usuario.usuario);
    return resp;
  } ));
}
logout(){
  localStorage.removeItem('token');
  localStorage.removeItem('expira');
  localStorage.removeItem('usuario');
}
private guardarUsuario(usuario:string){
this.usuario=usuario;
localStorage.setItem('usuario', usuario);
}
private guardarToken(idToken:string){
  this.userToken=idToken;
  localStorage.setItem('token',idToken);

  let hoy=new Date();
  hoy.setSeconds(3600);
  localStorage.setItem('expira',hoy.getTime().toString())
}
leerToken(){
  if(localStorage.getItem('token')){
    this.userToken=localStorage.getItem('token');
  }
  else{
    this.userToken='';
  }
}

estaAutenticado():boolean{
if(this.userToken=null){
  return false;
}
const expira = Number(localStorage.getItem('expira'));
const expiradate = new Date();
expiradate.setTime(expira);
if(expiradate>  new Date()){

  return true}
else{return false
  this.logout();}

}

}
