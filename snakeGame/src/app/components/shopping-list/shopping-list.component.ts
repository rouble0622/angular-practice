import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-shopping-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="shopping-list-container">
      <h2>Shopping List</h2>
      <ul>
        <li *ngFor="let product of products">{{ product }}</li>
      </ul>
      <div class="add-item">
        <input [(ngModel)]="newItem" placeholder="Add new item">
        <button (click)="addItem()">Add</button>
      </div>
    </div>
  `,
  styles: [`
    .shopping-list-container {
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 4px;
      margin: 20px;
      max-width: 400px;
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      padding: 8px;
      margin: 5px 0;
      background-color: #f8f9fa;
      border-radius: 4px;
    }
    .add-item {
      display: flex;
      gap: 10px;
      margin-top: 20px;
    }
    input {
      flex: 1;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      padding: 8px 16px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  `]
})
export class ShoppingListComponent {
  products: string[] = ["Milk", "Bread", "Cheese"];
  newItem: string = '';

  addItem() {
    if (this.newItem.trim()) {
      this.products.push(this.newItem);
      this.newItem = '';
    }
  }
} 