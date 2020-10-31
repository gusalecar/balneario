import { RouterModule, Routes } from '@angular/router';
import { ReservaComponent } from './componenet/reserva/reserva.component';
import { ReservaCroquisComponent } from './componenet/reserva-croquis/reserva-croquis.component';
import { ListareservasComponent } from './componenet/listareservas/listareservas.component';

import { ModalComponent } from './modal/modal.component';

import { AuthGuard } from './guard/auth.guard';
import { from } from 'rxjs';

const APP_ROUTES: Routes = [
  { path: 'home', component: ReservaComponent },
  { path: 'croquis', component: ReservaCroquisComponent },
  { path: 'verItems', component: ModalComponent },
  {
    path: 'listareservas',
    component: ListareservasComponent,
    canActivate: [AuthGuard],
  },
  { path: '**', pathMatch: 'full', redirectTo: 'home' },
];

export const APP_ROUTING = RouterModule.forRoot(APP_ROUTES);
