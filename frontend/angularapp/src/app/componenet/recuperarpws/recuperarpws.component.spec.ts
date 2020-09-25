import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecuperarpwsComponent } from './recuperarpws.component';

describe('RecuperarpwsComponent', () => {
  let component: RecuperarpwsComponent;
  let fixture: ComponentFixture<RecuperarpwsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecuperarpwsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecuperarpwsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
