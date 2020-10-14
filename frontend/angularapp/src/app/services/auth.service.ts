import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { UsuarioModel } from '../models/usuario.model';
import { map } from 'rxjs/operators';
import { ItemModel } from '../models/Item.model';
import { Observable } from 'rxjs';
import { DetallesModel } from '../models/detalles.model';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private url = 'http://localhost:8000/';
  userToken: string;
  usuario: string;
  constructor(private http: HttpClient) {}

  nuevoUsuario(usuario: UsuarioModel) {
    const authData = {
      username: usuario.usuario,
      email: usuario.mail,
      password: usuario.password,
    };
    return this.http.post(`${this.url}api/auth/register`, authData);
  }
  autenticarUsuario(usuario: UsuarioModel) {
    const authData2 = {
      username: usuario.usuario,
      password: usuario.password,
    };
    return this.http.post(`${this.url}api/auth/token`, authData2).pipe(
      map((resp) => {
        this.guardarToken(resp['access']);
        this.guardarUsuario(usuario.usuario);
        return resp;
      })
    );
  }
  //VER
  subirArchivo(File) {
    var json = JSON.stringify(File);
    console.log(json);
    console.log(File);
    this.userToken = localStorage.getItem('token');
    const headers = new HttpHeaders({
      Authorization: `Bearer ${this.userToken}`,
    });
    const authData2 = {
      reserva: 1,
      comprobante: json,
    };
    return this.http.post(`${this.url}api/transferencias`, authData2, {
      headers,
    });
  }
  verMisReservas() {
    this.userToken = localStorage.getItem('token');
    const headers = new HttpHeaders({
      Authorization: `Bearer ${this.userToken}`,
    });
    return this.http.get(`${this.url}api/reservas/`, { headers });
  }

  disponibilidadReeservable(
    fechaInicio: string,
    fechaFin: string
  ): Observable<ItemModel[]> {
    return this.http.get<ItemModel[]>(
      `${this.url}api/items/?fechainicio=${fechaInicio}&fechafin=${fechaFin}`
    );
  }
  reservar(reservables: DetallesModel[]) {
    this.userToken = localStorage.getItem('token');
    const headers = new HttpHeaders({
      Authorization: `Bearer ${this.userToken}`,
    });
    const reservaData = { detalles: reservables };
    console.log(reservaData);
    return this.http.post(`${this.url}api/reservas/`, reservaData, { headers });
  }

  getQuery(query: string) {
    const url = `${this.url}${query}`;
    const headers = new HttpHeaders({
      Authorization: `Bearer ${this.userToken}`,
    });
    return this.http.get(url, { headers });
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('expira');
    localStorage.removeItem('usuario');
  }
  private guardarUsuario(usuario: string) {
    this.usuario = usuario;
    localStorage.setItem('usuario', usuario);
  }
  private guardarToken(idToken: string) {
    this.userToken = idToken;
    localStorage.setItem('token', idToken);

    let hoy = new Date();
    hoy.setSeconds(3600);
    localStorage.setItem('expira', hoy.getTime().toString());
  }
  leerToken() {
    if (localStorage.getItem('token')) {
      this.userToken = localStorage.getItem('token');
    } else {
      this.userToken = '';
    }
  }

  estaAutenticado(): boolean {
    if (!localStorage.getItem('token')) {
      return false;
    }
    const expira = Number(localStorage.getItem('expira'));
    const expiradate = new Date();
    const actual = new Date();
    expiradate.setTime(expira);
    actual.setTime(Date.now());
    if (expiradate > actual) {
      return true;
    } else {
      this.logout();
      return false;
    }
  }
}
