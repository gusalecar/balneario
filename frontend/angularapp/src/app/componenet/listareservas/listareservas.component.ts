import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service'

@Component({
  selector: 'app-listareservas',
  templateUrl: './listareservas.component.html',
  styleUrls: ['./listareservas.component.css']
})
export class ListareservasComponent implements OnInit {

  constructor(private auth:AuthService) { }

  ngOnInit(): void {
    this.auth.verMisReservas().subscribe(resp=>{console.log(resp)})
  }

}
