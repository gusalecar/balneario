import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RespuestaCreacionCuentaComponent } from './respuesta-creacion-cuenta.component';

describe('RespuestaCreacionCuentaComponent', () => {
  let component: RespuestaCreacionCuentaComponent;
  let fixture: ComponentFixture<RespuestaCreacionCuentaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RespuestaCreacionCuentaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RespuestaCreacionCuentaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
