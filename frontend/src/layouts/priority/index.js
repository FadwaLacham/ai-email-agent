/**
=========================================================
* AI Email Agent - High Priority Emails
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

function Priority() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    api
      .get("https://ai-email-agent-backend.fastapicloud.dev/high-priority")

      .then((response) => {
        setEmails(response.data);
      })

      .catch((error) => {
        console.log("High Priority API Error:", error);
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
                <MDTypography variant="h5">🚨 High Priority Emails</MDTypography>

                <MDTypography variant="button" color="text">
                  Emails detected as urgent by AI Agent
                </MDTypography>
              </MDBox>

              <MDBox p={3}>
                {emails.length === 0 ? (
                  <MDTypography>No high priority emails found</MDTypography>
                ) : (
                  emails.map((email, index) => (
                    <Card
                      key={index}
                      sx={{
                        mb: 2,
                        p: 2,
                      }}
                    >
                      <MDTypography variant="h6">📩 {email.subject}</MDTypography>

                      <MDTypography variant="body2">Sender: {email.sender}</MDTypography>

                      <MDTypography variant="body2">AI Score: {email.score}</MDTypography>

                      <MDBox mt={1}>
                        <MDTypography variant="button" color="error">
                          Decision: {email.decision}
                        </MDTypography>
                      </MDBox>
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

export default Priority;
