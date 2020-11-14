import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { ReservaComponent } from './componenet/reserva/reserva.component';

import { NavbarComponent } from './componenet/navbar/navbar.component';
import { FooterComponent } from './componenet/footer/footer.component';

import { APP_ROUTING } from './app.routes';
import { ReservaCroquisComponent } from './componenet/reserva-croquis/reserva-croquis.component';

import { FormsModule } from '@angular/forms';

import { HttpClientModule } from '@angular/common/http';
import { ListareservasComponent } from './componenet/listareservas/listareservas.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { PagoComponent } from './componenet/pago/pago.component';
import {
  SocialLoginModule,
  SocialAuthServiceConfig,
} from 'angularx-social-login';
import { FacebookLoginProvider } from 'angularx-social-login';

@NgModule({
  declarations: [
    AppComponent,
    ReservaComponent,
    NavbarComponent,
    FooterComponent,
    ReservaCroquisComponent,
    ListareservasComponent,
    PagoComponent,
  ],
  imports: [
    HttpClientModule,
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    APP_ROUTING,
    BrowserAnimationsModule,
    SocialLoginModule,
  ],
  providers: [
    {
      provide: 'SocialAuthServiceConfig',
      useValue: {
        autoLogin: false,
        providers: [
          {
            id: FacebookLoginProvider.PROVIDER_ID,
            provider: new FacebookLoginProvider('684437409159465'),
          },
        ],
      } as SocialAuthServiceConfig,
    },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
