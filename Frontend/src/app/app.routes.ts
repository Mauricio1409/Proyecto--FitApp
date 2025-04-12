import { Routes } from '@angular/router';
import HomePageComponent from './shared/pages/Home-page/Home-page.component';

export const routes: Routes = [

  {
    path: 'home',
    loadComponent : () => import('./shared/pages/Home-page/Home-page.component')
  },
  {
    path : '**',
    component : HomePageComponent
  }

];
