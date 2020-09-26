import { Component, OnInit } from '@angular/core';
import { Router} from '@angular/router'
@Component({
  selector: 'app-reserva',
  templateUrl: './reserva.component.html',
  styleUrls: ['./reserva.component.css']
})
export class ReservaComponent implements OnInit {
mostrarCov19:boolean=true;
  constructor(private router:Router) { }

  ngOnInit(): void {
  }
  irCrouis(){
    this.router.navigateByUrl('/croquis');
  }
}
