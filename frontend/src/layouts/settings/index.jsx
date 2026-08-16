/**
=========================================================
* AI Email Agent - Agent Settings
=========================================================
*/

import { useEffect, useState } from "react";

import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import TextField from "@mui/material/TextField";
import MenuItem from "@mui/material/MenuItem";
import Switch from "@mui/material/Switch";
import Button from "@mui/material/Button";

import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";

import api from "api/axios";

function Settings() {
  const [settings, setSettings] = useState({
    model: "gemini",

    temperature: 0.7,

    max_emails: 100,

    auto_action: true,
  });

  useEffect(() => {
    api

      .get("https://ai-email-agent-backend.fastapicloud.dev/settings")

      .then((response) => {
        setSettings(response.data);
      })

      .catch(console.log);
  }, []);

  const handleChange = (field, value) => {
    setSettings({
      ...settings,

      [field]: value,
    });
  };

  const saveSettings = () => {
    api

      .put(
        "https://ai-email-agent-backend.fastapicloud.dev/settings",

        settings
      )

      .then(() => {
        alert("Settings updated successfully");
      })

      .catch(console.log);
  };

  return (
    <DashboardLayout>
      <DashboardNavbar />

      <MDBox pt={6} pb={3}>
        <Grid container spacing={6}>
          <Grid item xs={12}>
            <Card>
              <MDBox
                mx={2}
                mt={-3}
                py={3}
                px={2}
                variant="gradient"
                bgColor="info"
                borderRadius="lg"
                coloredShadow="info"
              >
                <MDTypography variant="h6" color="white">
                  🤖 Agent Settings
                </MDTypography>
              </MDBox>

              <MDBox p={3}>
                <Grid container spacing={3}>
                  <Grid item xs={12} md={6}>
                    <TextField
                      select
                      fullWidth
                      label="AI Model"
                      value={settings.model}
                      onChange={(e) => handleChange("model", e.target.value)}
                    >
                      <MenuItem value="gemini">Gemini</MenuItem>

                      <MenuItem value="gpt">GPT</MenuItem>
                    </TextField>
                  </Grid>

                  <Grid item xs={12} md={6}>
                    <TextField
                      fullWidth
                      type="number"
                      label="Temperature"
                      value={settings.temperature}
                      onChange={(e) =>
                        handleChange(
                          "temperature",

                          Number(e.target.value)
                        )
                      }
                    />
                  </Grid>

                  <Grid item xs={12} md={6}>
                    <TextField
                      fullWidth
                      type="number"
                      label="Maximum Emails"
                      value={settings.max_emails}
                      onChange={(e) =>
                        handleChange(
                          "max_emails",

                          Number(e.target.value)
                        )
                      }
                    />
                  </Grid>

                  <Grid item xs={12} md={6}>
                    <MDTypography variant="button">Automatic Actions</MDTypography>

                    <br />

                    <Switch
                      checked={settings.auto_action}
                      onChange={(e) =>
                        handleChange(
                          "auto_action",

                          e.target.checked
                        )
                      }
                    />
                  </Grid>

                  <Grid item xs={12}>
                    <Button variant="contained" color="info" onClick={saveSettings}>
                      SAVE SETTINGS
                    </Button>
                  </Grid>
                </Grid>
              </MDBox>
            </Card>
          </Grid>
        </Grid>
      </MDBox>

      <Footer />
    </DashboardLayout>
  );
}

export default Settings;
