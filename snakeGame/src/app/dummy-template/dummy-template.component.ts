import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../services/api.service';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-dummy-template',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './dummy-template.component.html',
  styleUrls: ['./dummy-template.component.css']
})
export class DummyTemplateComponent implements OnInit {
  title = 'Dummy Template';
  products: string[] = ["Milk", "Bread", "Cheese"];
  items: string[] = ["Milk", "Bread", "Cheese"];
  nodeData: any = null;
  pythonData: any = null;
  newItem: string = '';
  loading = false;
  error: string | null = null;
  
  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    console.log('Dummy Template Component Initialized');
  }
  
  addItem() {
    if (this.newItem.trim()) {
      this.products.push(this.newItem);
      this.newItem = '';
    }
  }

  removeItem(item: string) {
    this.products = this.products.filter(i => i !== item);
  }
} 