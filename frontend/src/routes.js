import Dashboard from "layouts/dashboard";
import Tables from "layouts/tables";
import Notifications from "layouts/notifications";
import Profile from "layouts/profile";
import Priority from "layouts/priority";
import Actions from "layouts/actions";
import Monitoring from "layouts/monitoring";
import Analytics from "layouts/Analytics";
import Settings from "layouts/settings";
import SignIn from "layouts/authentication/sign-in";

import Icon from "@mui/material/Icon";

const routes = [
  {
    type: "collapse",
    name: "Dashboard",
    key: "dashboard",
    icon: <Icon fontSize="small">dashboard</Icon>,
    route: "/dashboard",
    component: <Dashboard />,
  },

  {
    type: "collapse",
    name: "Emails",
    key: "emails",
    icon: <Icon fontSize="small">email</Icon>,
    route: "/emails",
    component: <Tables />,
  },

  {
    type: "collapse",
    name: "High Priority",
    key: "priority",
    icon: <Icon fontSize="small">priority_high</Icon>,
    route: "/priority",
    component: <Priority />,
  },

  {
    type: "collapse",
    name: "Agent Actions",
    key: "actions",
    icon: <Icon fontSize="small">smart_toy</Icon>,
    route: "/actions",
    component: <Actions />,
  },

  {
    type: "collapse",
    name: "AI Notifications",
    key: "notifications",
    icon: <Icon fontSize="small">notifications</Icon>,
    route: "/notifications",
    component: <Notifications />,
  },

  {
    type: "collapse",
    name: "Monitoring",
    key: "monitoring",
    icon: <Icon fontSize="small">monitoring</Icon>,
    route: "/monitoring",
    component: <Monitoring />,
  },

  {
    type: "collapse",
    name: "Analytics",
    key: "analytics",
    icon: <Icon fontSize="small">analytics</Icon>,
    route: "/analytics",
    component: <Analytics />,
  },

  {
    type: "collapse",
    name: "Agent Settings",
    key: "settings",
    icon: <Icon fontSize="small">settings</Icon>,
    route: "/settings",
    component: <Settings />,
  },

  {
    type: "collapse",
    name: "Profile",
    key: "profile",
    icon: <Icon fontSize="small">person</Icon>,
    route: "/profile",
    component: <Profile />,
  },

  {
    type: "route",
    name: "Sign In",
    key: "sign-in",
    route: "/authentication/sign-in",
    component: <SignIn />,
  },
];

export default routes;
