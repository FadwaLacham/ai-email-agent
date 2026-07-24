/**
=========================================================
* AI Email Agent - Login Page
=========================================================
*/

import { useState } from "react";

import { Link, useNavigate } from "react-router-dom";

import Card from "@mui/material/Card";
import Switch from "@mui/material/Switch";

import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDInput from "components/MDInput";
import MDButton from "components/MDButton";

import BasicLayout from "layouts/authentication/components/BasicLayout";

import bgImage from "assets/images/bg-sign-in-basic.jpeg";

import api from "api/axios";

function Basic() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [rememberMe, setRememberMe] = useState(false);

  const [error, setError] = useState("");

  const handleSetRememberMe = () => {
    setRememberMe(!rememberMe);
  };

  const handleLogin = async (event) => {
    event.preventDefault();

    setError("");

    try {
      // supprimer ancien token
      localStorage.removeItem("token");

      const response = await api.post("/auth/login", {
        email: email,
        password: password,
      });

      console.log("LOGIN RESPONSE :", response.data);

      if (response.data.access_token) {
        localStorage.setItem("token", response.data.access_token);

        console.log("TOKEN SAVED :", localStorage.getItem("token"));

        navigate("/dashboard");
      } else {
        setError("Invalid email or password");
      }
    } catch (error) {
      console.log("LOGIN ERROR :", error);

      setError("Login failed");
    }
  };

  return (
    <BasicLayout image={bgImage}>
      <Card>
        <MDBox
          variant="gradient"
          bgColor="info"
          borderRadius="lg"
          coloredShadow="info"
          mx={2}
          mt={-3}
          p={2}
          mb={1}
          textAlign="center"
        >
          <MDTypography variant="h4" fontWeight="medium" color="white" mt={1}>
            AI Email Agent
          </MDTypography>
        </MDBox>

        <MDBox pt={4} pb={3} px={3}>
          <MDBox component="form" role="form" onSubmit={handleLogin}>
            {error && (
              <MDTypography color="error" variant="button">
                {error}
              </MDTypography>
            )}

            <MDBox mb={2}>
              <MDInput
                type="email"
                label="Email"
                fullWidth
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </MDBox>

            <MDBox mb={2}>
              <MDInput
                type="password"
                label="Password"
                fullWidth
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </MDBox>

            <MDBox display="flex" alignItems="center" ml={-1}>
              <Switch checked={rememberMe} onChange={handleSetRememberMe} />

              <MDTypography
                variant="button"
                fontWeight="regular"
                sx={{
                  cursor: "pointer",

                  userSelect: "none",

                  ml: -1,
                }}
                onClick={handleSetRememberMe}
              >
                &nbsp;&nbsp;Remember me
              </MDTypography>
            </MDBox>

            <MDBox mt={4} mb={1}>
              <MDButton type="submit" variant="gradient" color="info" fullWidth>
                SIGN IN
              </MDButton>
            </MDBox>

            <MDBox mt={3} mb={1} textAlign="center">
              <MDTypography variant="button" color="text">
                Don&apos;t have an account?{" "}
                <MDTypography
                  component={Link}
                  to="/authentication/sign-up"
                  variant="button"
                  color="info"
                  fontWeight="medium"
                  textGradient
                >
                  Sign up
                </MDTypography>
              </MDTypography>
            </MDBox>
          </MDBox>
        </MDBox>
      </Card>
    </BasicLayout>
  );
}

export default Basic;
