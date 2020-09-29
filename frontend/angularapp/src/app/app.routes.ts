import {  RouterModule, Routes } from '@angular/router'
import { ReservaComponent} from './componenet/reserva/reserva.component'
import { RecuperarpwsComponent } from './componenet/recuperarpws/recuperarpws.component'
import { RespuestaCreacionCuentaComponent } from './componenet/respuesta-creacion-cuenta/respuesta-creacion-cuenta.component'
import { ReservaCroquisComponent} from './componenet/reserva-croquis/reserva-croquis.component'
import { ReservapagoComponent } from './componenet/reservapago/reservapago.component'

import { AuthGuard} from './guard/auth.guard'

const APP_ROUTES: Routes =[
    {path: 'home', component: ReservaComponent},
    {path: 'pwd', component:RecuperarpwsComponent},
    {path: 'newacc', component:RespuestaCreacionCuentaComponent},
    {path: 'croquis', component:ReservaCroquisComponent},
    {path: 'pago', component:ReservapagoComponent, canActivate:[AuthGuard]},
    {path:'**', pathMatch:'full', redirectTo: 'home'}
];

export const APP_ROUTING = RouterModule.forRoot(APP_ROUTES)
