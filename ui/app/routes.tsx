import { type RouteConfig, index, route } from '@react-router/dev/routes';

export default [
  index('features/welcome/WelcomePage.tsx'),
  route('/chat', 'features/chat/ChatView.tsx')
] satisfies RouteConfig;
