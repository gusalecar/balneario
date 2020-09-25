import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReservaCroquisComponent } from './reserva-croquis.component';

describe('ReservaCroquisComponent', () => {
  let component: ReservaCroquisComponent;
  let fixture: ComponentFixture<ReservaCroquisComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReservaCroquisComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReservaCroquisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
