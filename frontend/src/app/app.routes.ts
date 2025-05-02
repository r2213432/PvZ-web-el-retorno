import { Routes } from '@angular/router';
import { PvzMComponent } from './pages/pvz-m/pvz-m.component';
import { PvzAComponent } from './pages/pvz-a/pvz-a.component';

export const routes: Routes = [
    { path: 'hola', component:PvzMComponent, pathMatch: 'full'},
    { path: 'AlmanaquePlantas', component:PvzAComponent, pathMatch: 'full'},
    {path: '**', redirectTo: 'hola'}
];
