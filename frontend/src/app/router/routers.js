import Base from '../../app';
import { KanbanBoard } from '../components';


export default [{
    path: '/',
    component: Base,
    children: [{
        path: '/',
        component: KanbanBoard
    }, ]
}, ]