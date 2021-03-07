import Base from '../../app';
import { Signin, KanbanBoard } from '../components';


export default [{
    path: '/',
    component: Base,
    children: [{
            path: '/',
            component: KanbanBoard
        },
        {
            path: 'signin',
            component: Signin
        }
    ]
}, ]