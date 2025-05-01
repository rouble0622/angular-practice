import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  // Update these URLs according to your API endpoints
  //private nodeApiUrl = 'http://localhost:3000/api';
  private pythonApiUrl = 'http://localhost:5000/api';

  constructor(
    private http: HttpClient,
    private authService: AuthService
  ) { }

  // // Node.js API calls
  // getNodeData(): Observable<any> {
  //   return this.http.get(`${this.nodeApiUrl}/data`);
  // }

  // postNodeData(data: any): Observable<any> {
  //   return this.http.post(`${this.nodeApiUrl}/data`, data);
  // }

  // Python API calls
  getPythonData(): Observable<any> {
    const token = this.authService.getToken();
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });

    return this.http.get(`${this.pythonApiUrl}/protected`, { headers: headers });
  }

  postPythonData(data: any): Observable<any> {
    return this.http.post(`${this.pythonApiUrl}/login`, data);
  }

  postPythonRegister(data: any): Observable<any> {
    return this.http.post(`${this.pythonApiUrl}/register`, data);
  }
} 