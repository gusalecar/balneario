import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from'@angular/router';
import { param } from 'jquery';

@Component({
  selector: 'app-reservapago',
  templateUrl: './reservapago.component.html',
  styleUrls: ['./reservapago.component.css']
})
export class ReservapagoComponent implements OnInit {

total:number=0;
cbu:number=241243124234124312431;

  constructor(private router:Router, private route:ActivatedRoute ) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(param=>{
      if( param.has('total')){
        this.total= Number(param.get('total'))*0.3;
      }
    })
  }

}
