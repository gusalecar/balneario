import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Action } from 'rxjs/internal/scheduler/Action';

declare var paypal;

@Component({
  selector: 'app-pago',
  templateUrl: './pago.component.html',
  styleUrls: ['./pago.component.css']
})
export class PagoComponent implements OnInit {
  id: number;
@ViewChild('paypal', {static: true})paypalElement: ElementRef;
producto={
  descripcion:'asfdsdafas',
  precio: 1,
  img: 'imagen de tu producto'
}
  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    this.producto.precio = +this.route.snapshot.queryParamMap.get('id');

    paypal.Buttons({
      createOrder:(data, actions)=>{
        return actions.order.create({
          purchase_units:[{
            description: this.producto.descripcion,
            amount:{
              currency_code:'USD',
              value: this.producto.precio
            }
          }]
        })
      },
      onApprove: async (data, actions)=>{
        const order= await actions.order.capture();
        console.log(order);

      },
      onError: err =>{
        console.log(err)
      }
    }
    ).render(this.paypalElement.nativeElement);
  }

}
