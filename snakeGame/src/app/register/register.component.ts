import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../services/api.service';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  registerForm: FormGroup;
  loading = false;
  error: string | null = null;
  
  constructor(
    private fb: FormBuilder,
    private apiService: ApiService,
    private router: Router,
    private authService: AuthService
  ) {
    this.registerForm = this.fb.group({
      username: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]]
    });
  }

  ngOnInit(): void {
    // If already logged in, redirect to home
    if (this.authService.isAuthenticated()) {
      this.router.navigate(['/dashboard']);
    }
  }

  onSubmit() {
    if (this.registerForm.valid) {
      this.loading = true;
      this.error = null;
      
      const formData = this.registerForm.value;
      this.apiService.postPythonRegister(formData).subscribe({
        next: (response) => {
          console.log('Register successful:', response);          
          this.router.navigate(['/login']);
          // if (response.access_token) {
          //   this.authService.setToken(response.access_token);
          //   this.router.navigate(['/']); // Redirect to home after successful login
          // }
          this.loading = false;
        },
        error: (err) => {
          console.error('Register error:', err);
          this.error = err.error?.message || 'Register failed. Please try again.';
          this.loading = false;
        }
      });
    }
  }
} 