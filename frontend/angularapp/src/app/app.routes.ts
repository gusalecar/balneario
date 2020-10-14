import { RouterModule, Routes } from '@angular/router';
import { ReservaComponent } from './componenet/reserva/reserva.component';
import { RecuperarpwsComponent } from './componenet/recuperarpws/recuperarpws.component';
import { RespuestaCreacionCuentaComponent } from './componenet/respuesta-creacion-cuenta/respuesta-creacion-cuenta.component';
import { ReservaCroquisComponent } from './componenet/reserva-croquis/reserva-croquis.component';
import { ReservapagoComponent } from './componenet/reservapago/reservapago.component';
import { ListareservasComponent } from './componenet/listareservas/listareservas.component';

import { AuthGuard } from './guard/auth.guard';
import { from } from 'rxjs';

const APP_ROUTES: Routes = [
  { path: 'home', component: ReservaComponent },
  { path: 'pwd', component: RecuperarpwsComponent },
  { path: 'newacc', component: RespuestaCreacionCuentaComponent },
  { path: 'croquis', component: ReservaCroquisComponent },
  {
    path: 'posreserva/:total',
    component: ReservapagoComponent,
    canActivate: [AuthGuard],
  },
  {
    path: 'listareservas',
    component: ListareservasComponent,
    canActivate: [AuthGuard],
  },
  { path: '**', pathMatch: 'full', redirectTo: 'home' },
];

export const APP_ROUTING = RouterModule.forRoot(APP_ROUTES);
