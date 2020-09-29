import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { from } from 'rxjs';

import { ReservaComponent } from './componenet/reserva/reserva.component'
import { RecuperarpwsComponent } from './componenet/recuperarpws/recuperarpws.component'

const routes: Routes = [
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
 

 }
