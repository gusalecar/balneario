import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReservapagoComponent } from './reservapago.component';

describe('ReservapagoComponent', () => {
  let component: ReservapagoComponent;
  let fixture: ComponentFixture<ReservapagoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ReservapagoComponent],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReservapagoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
