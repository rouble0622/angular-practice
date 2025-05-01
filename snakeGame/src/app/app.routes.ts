import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { GameComponent } from './components/game/game.component';
import { SettingsComponent } from './components/settings/settings.component';
import { LoginComponent } from './login/login.component';
import { AuthGuard } from './guards/auth.guard';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { LogoutComponent } from './components/logout/logout.component';
import { RegisterComponent } from './register/register.component';
import { DummyTemplateComponent } from './dummy-template/dummy-template.component';
export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'dummy-template', component: DummyTemplateComponent },
  { path: 'logout', component: LogoutComponent },
  { 
    path: '', 
    component: HomeComponent    
  },
  { 
    path: 'dashboard', 
    component: DashboardComponent,
    canActivate: [AuthGuard]
  },
  { 
    path: 'game', 
    component: GameComponent,
    canActivate: [AuthGuard]
  },  
  { 
    path: 'settings', 
    component: SettingsComponent,
    canActivate: [AuthGuard]
  },
  { path: '**', redirectTo: '' }
];
