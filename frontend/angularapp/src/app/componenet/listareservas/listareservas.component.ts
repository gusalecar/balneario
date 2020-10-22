import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-listareservas',
  templateUrl: './listareservas.component.html',
  styleUrls: ['./listareservas.component.css'],
})
export class ListareservasComponent implements OnInit {
  reservas: any;
  file: File;
  constructor(private auth: AuthService) {}

  ngOnInit(): void {
    this.auth.verMisReservas().subscribe((resp) => {
      console.log(resp);
      this.reservas = resp;
    });
  }
  fileEvent(fileInput: Event) {
    this.file = (<HTMLInputElement>fileInput.target).files[0];
  }
  subirArchivo() {
    this.auth.subirArchivo(this.file).subscribe((res) => {
      console.log(res);
    });
  }
}
