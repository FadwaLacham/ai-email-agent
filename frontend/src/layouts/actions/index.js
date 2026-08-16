/**
=========================================================
* AI Email Agent - Agent Actions
=========================================================
*/

import { useEffect, useState } from "react";

import api from "api/axios";

import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";

import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

function Actions() {
  const [actions, setActions] = useState([]);

  useEffect(() => {
    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/actions")

      .then((response) => {
        setActions(response.data);
      })

      .catch((error) => {
        console.log("Actions API Error:", error);
      });
  }, []);

  return (
    <DashboardLayout>
      <DashboardNavbar />

      <MDBox py={3}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Card>
              <MDBox p={3}>
                <MDTypography variant="h5">🤖 Agent Actions</MDTypography>

                <MDTypography variant="button" color="text">
                  Actions automatically executed by AI Agent
                </MDTypography>
              </MDBox>

              <MDBox p={3}>
                {actions.length === 0 ? (
                  <MDTypography>No actions available</MDTypography>
                ) : (
                  actions.map((action, index) => (
                    <Card
                      key={index}
                      sx={{
                        mb: 2,
                        p: 2,
                      }}
                    >
                      <MDTypography variant="h6">⚡ {action.action}</MDTypography>

                      <MDTypography variant="body2">Executed: {action.count} times</MDTypography>
                    </Card>
                  ))
                )}
              </MDBox>
            </Card>
          </Grid>
        </Grid>
      </MDBox>

      <Footer />
    </DashboardLayout>
  );
}

export default Actions;
