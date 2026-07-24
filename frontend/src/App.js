/**
=========================================================
* Material Dashboard 2 React - AI Email Agent
=========================================================
*/

import { useState, useEffect, useMemo } from "react";

import { Routes, Route, Navigate, useLocation } from "react-router-dom";

import { ThemeProvider } from "@mui/material/styles";

import CssBaseline from "@mui/material/CssBaseline";

import Icon from "@mui/material/Icon";

import MDBox from "components/MDBox";

import Sidenav from "examples/Sidenav";

import Configurator from "examples/Configurator";

import theme from "assets/theme";

import themeRTL from "assets/theme/theme-rtl";

import themeDark from "assets/theme-dark";

import themeDarkRTL from "assets/theme-dark/theme-rtl";

import rtlPlugin from "stylis-plugin-rtl";

import { CacheProvider } from "@emotion/react";

import createCache from "@emotion/cache";

import routes from "routes";

import { useMaterialUIController, setMiniSidenav, setOpenConfigurator } from "context";

import brandWhite from "assets/images/logo-ct.png";

import brandDark from "assets/images/logo-ct-dark.png";

import SignIn from "layouts/authentication/sign-in";

import SignUp from "layouts/authentication/sign-up";

import ProtectedRoute from "components/ProtectedRoute";

export default function App() {
  const [controller, dispatch] = useMaterialUIController();

  const {
    miniSidenav,
    direction,
    layout,
    openConfigurator,
    sidenavColor,
    transparentSidenav,
    whiteSidenav,
    darkMode,
  } = controller;

  const [onMouseEnter, setOnMouseEnter] = useState(false);

  const [rtlCache, setRtlCache] = useState(null);

  const { pathname } = useLocation();

  useMemo(() => {
    const cacheRtl = createCache({
      key: "rtl",

      stylisPlugins: [rtlPlugin],
    });

    setRtlCache(cacheRtl);
  }, []);

  const handleOnMouseEnter = () => {
    if (miniSidenav && !onMouseEnter) {
      setMiniSidenav(dispatch, false);

      setOnMouseEnter(true);
    }
  };

  const handleOnMouseLeave = () => {
    if (onMouseEnter) {
      setMiniSidenav(dispatch, true);

      setOnMouseEnter(false);
    }
  };

  const handleConfiguratorOpen = () => {
    setOpenConfigurator(dispatch, !openConfigurator);
  };

  useEffect(() => {
    document.body.setAttribute("dir", direction);
  }, [direction]);

  useEffect(() => {
    document.documentElement.scrollTop = 0;

    document.scrollingElement.scrollTop = 0;
  }, [pathname]);

  // ================= PRIVATE ROUTES =================

  const getRoutes = (allRoutes) =>
    allRoutes.map((route) => {
      if (route.collapse) {
        return getRoutes(route.collapse);
      }

      if (route.route) {
        return (
          <Route
            key={route.key}
            path={route.route}
            element={<ProtectedRoute>{route.component}</ProtectedRoute>}
          />
        );
      }

      return null;
    });

  const configsButton = (
    <MDBox
      display="flex"
      justifyContent="center"
      alignItems="center"
      width="3.25rem"
      height="3.25rem"
      bgColor="white"
      shadow="sm"
      borderRadius="50%"
      position="fixed"
      right="2rem"
      bottom="2rem"
      zIndex={99}
      color="dark"
      sx={{
        cursor: "pointer",
      }}
      onClick={handleConfiguratorOpen}
    >
      <Icon fontSize="small">settings</Icon>
    </MDBox>
  );

  const content = (
    <>
      {/* SIDEBAR */}

      {layout === "dashboard" &&
        pathname !== "/authentication/sign-in" &&
        pathname !== "/authentication/sign-up" &&
        localStorage.getItem("token") && (
          <>
            <Sidenav
              color={sidenavColor}
              brand={(transparentSidenav && !darkMode) || whiteSidenav ? brandDark : brandWhite}
              brandName="AI Email Agent"
              routes={routes}
              onMouseEnter={handleOnMouseEnter}
              onMouseLeave={handleOnMouseLeave}
            />

            <Configurator />

            {configsButton}
          </>
        )}

      <Routes>
        {/* PUBLIC ROUTES */}

        <Route path="/authentication/sign-in" element={<SignIn />} />

        <Route path="/authentication/sign-up" element={<SignUp />} />

        {/* PRIVATE ROUTES */}

        {getRoutes(routes)}

        {/* DEFAULT */}

        <Route path="*" element={<Navigate to="/authentication/sign-in" replace />} />
      </Routes>
    </>
  );

  return direction === "rtl" ? (
    <CacheProvider value={rtlCache}>
      <ThemeProvider theme={darkMode ? themeDarkRTL : themeRTL}>
        <CssBaseline />

        {content}
      </ThemeProvider>
    </CacheProvider>
  ) : (
    <ThemeProvider theme={darkMode ? themeDark : theme}>
      <CssBaseline />

      {content}
    </ThemeProvider>
  );
}
