/**
=========================================================
* AI Email Agent - Notifications Page
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

function Notifications() {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/notifications")

      .then((response) => {
        setNotifications(response.data);
      })

      .catch((error) => {
        console.log("Notification API Error:", error);
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
                <MDTypography variant="h5">🔔 AI Notifications</MDTypography>

                <MDTypography variant="button" color="text">
                  Notifications generated automatically by AI Email Agent
                </MDTypography>
              </MDBox>

              <MDBox p={3}>
                {notifications.length === 0 ? (
                  <MDTypography>No notifications available</MDTypography>
                ) : (
                  notifications.map((notification) => (
                    <Card
                      key={notification.id}
                      sx={{
                        mb: 2,
                        p: 2,
                      }}
                    >
                      <MDTypography variant="h6">📩 {notification.subject}</MDTypography>

                      <MDTypography variant="body2" color="text">
                        {notification.message}
                      </MDTypography>

                      <MDBox mt={1}>
                        <MDTypography variant="button" color="success">
                          Status: {notification.status}
                        </MDTypography>
                      </MDBox>

                      <MDTypography variant="caption" color="text">
                        Date: {notification.date}
                      </MDTypography>
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

export default Notifications;
