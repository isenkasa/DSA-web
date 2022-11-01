import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ArrayView from '../views/ArrayView.vue'
import StringView from '../views/StringView.vue'
import LinkedListView from '../views/LinkedListView.vue'
import StackView from '../views/StackView.vue'
import HeapView from '../views/HeapView.vue'
import TreeView from '../views/TreeView.vue'
import GraphView from '../views/GraphView.vue'
import AdvancedGraphView from '../views/AdvancedGraphView.vue'
import IntervalView from '../views/IntervalView.vue'
import BacktrackingView from '../views/BacktrackingView.vue'
import DynamicProgrammingView from '../views/DynamicProgrammingView.vue'
import GreedyAlgorithmView from '../views/GreedyAlgorithmView.vue'
import MathView from '../views/MathView.vue'
import BitView from '../views/BitView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/array',
    name: 'array',
    component: ArrayView
  },
  {
    path: '/string',
    name: 'string',
    component: StringView
  },
  {
    path: '/linked-list',
    name: 'linked-list',
    component: LinkedListView
  },
  {
    path: '/stack',
    name: 'stack',
    component: StackView
  },
  {
    path: '/heap',
    name: 'heap',
    component: HeapView
  },
  {
    path: '/tree',
    name: 'tree',
    component: TreeView
  },
  {
    path: '/graph',
    name: 'graph',
    component: GraphView
  },
  {
    path: '/advanced-graph',
    name: 'advanced-graph',
    component: AdvancedGraphView
  },
  {
    path: '/interval',
    name: 'interval',
    component: IntervalView
  },
  {
    path: '/backtracking',
    name: 'backtracking',
    component: BacktrackingView
  },
  {
    path: '/dynamic-programming',
    name: 'dynamic-programming',
    component: DynamicProgrammingView
  },
  {
    path: '/greedy-algorithm',
    name: 'greedy-algorithm',
    component: GreedyAlgorithmView
  },
  {
    path: '/math',
    name: 'math',
    component: MathView
  },
  {
    path: '/bit',
    name: 'bit',
    component: BitView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
