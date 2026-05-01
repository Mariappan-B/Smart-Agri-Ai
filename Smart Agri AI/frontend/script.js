const translations = {
    en: {
        title: "<span class='highlight'>Smart</span> Agri AI",
        subtitle: "Predict the most profitable crop for your land using advanced AI.",
        soil_info_title: "🌱 Soil Information",
        soil_color: "🎨 Soil Color",
        select_color: "Select soil color",
        color_black: "Black (Rich, fertile)",
        color_red: "Red (Iron-rich)",
        color_brown: "Brown (Balanced)",
        color_sandy: "Sandy (Loose)",
        soil_texture: "🤏 Soil Texture",
        select_texture: "Select texture",
        tex_sticky: "Sticky (Clay-like)",
        tex_soft: "Soft (Loamy)",
        tex_grainy: "Grainy (Sandy)",
        water_retention: "💧 Water Retention",
        select_retention: "Select retention",
        ret_high: "High (Stays wet long)",
        ret_medium: "Medium",
        ret_low: "Low (Dries fast)",
        location_title: "📍 Location & Weather",
        location_helper: "We need your location to fetch real-time weather data.",
        btn_location: "Get Current Location",
        btn_predict: "Predict Best Crop",
        loading_text: "Analyzing soil and weather data...",
        results_title: "🤖 AI Prediction Results",
        res_best_crop: "🌾 Best Crop to Plant",
        res_profitable: "💰 Top 3 Profitable Alternatives",
        res_env: "🌦️ Environmental Snapshot",
        btn_reset: "Start Over"
    },
    hi: {
        title: "<span class='highlight'>स्मार्ट</span> एग्री एआई",
        subtitle: "उन्नत एआई का उपयोग करके अपनी भूमि के लिए सबसे अधिक लाभदायक फसल की भविष्यवाणी करें।",
        soil_info_title: "🌱 मिट्टी की जानकारी",
        soil_color: "🎨 मिट्टी का रंग",
        select_color: "रंग चुनें",
        color_black: "काला (उपजाऊ)",
        color_red: "लाल (लौह युक्त)",
        color_brown: "भूरा (संतुलित)",
        color_sandy: "रेतीला (ढीला)",
        soil_texture: "🤏 मिट्टी की बनावट",
        select_texture: "बनावट चुनें",
        tex_sticky: "चिपचिपी",
        tex_soft: "नरम",
        tex_grainy: "दानेदार (रेतीली)",
        water_retention: "💧 जल प्रतिधारण क्षमता",
        select_retention: "क्षमता चुनें",
        ret_high: "उच्च (लंबे समय तक गीली)",
        ret_medium: "मध्यम",
        ret_low: "कम (जल्दी सूखने वाली)",
        location_title: "📍 स्थान और मौसम",
        location_helper: "मौसम डेटा प्राप्त करने के लिए हमें आपके स्थान की आवश्यकता है।",
        btn_location: "वर्तमान स्थान प्राप्त करें",
        btn_predict: "सर्वश्रेष्ठ फसल की भविष्यवाणी करें",
        loading_text: "मिट्टी और मौसम के डेटा का विश्लेषण हो रहा है...",
        results_title: "🤖 एआई भविष्यवाणी परिणाम",
        res_best_crop: "🌾 उगाने के लिए सर्वश्रेष्ठ फसल",
        res_profitable: "💰 शीर्ष 3 लाभदायक विकल्प",
        res_env: "🌦️ पर्यावरण स्नैपशॉट",
        btn_reset: "फिर से शुरू करें"
    },
    ta: {
        title: "<span class='highlight'>ஸ்மார்ட்</span> அக்ரி ஏஐ",
        subtitle: "நவீன AI-யைப் பயன்படுத்தி உங்கள் நிலத்திற்கான சிறந்த பயிரைக் கண்டறியவும்.",
        soil_info_title: "🌱 மண் விவரங்கள்",
        soil_color: "🎨 மண்ணின் நிறம்",
        select_color: "நிறத்தை தேர்ந்தெடுக்கவும்",
        color_black: "கருப்பு (வளமான)",
        color_red: "சிவப்பு (இரும்புச் சத்து)",
        color_brown: "பழுப்பு (சீரான)",
        color_sandy: "மணல் (தளர்வான)",
        soil_texture: "🤏 மண்ணின் அமைப்பு",
        select_texture: "அமைப்பைத் தேர்ந்தெடுக்கவும்",
        tex_sticky: "ஒட்டும் தன்மை",
        tex_soft: "மென்மையான",
        tex_grainy: "பருமனான (மணல்)",
        water_retention: "💧 நீர் தேக்கத் திறன்",
        select_retention: "திறனைத் தேர்ந்தெடுக்கவும்",
        ret_high: "அதிகம் (நீண்ட நேரம் ஈரப்பதம்)",
        ret_medium: "நடுத்தரம்",
        ret_low: "குறைவு (விரைவில் காய்ந்துவிடும்)",
        location_title: "📍 இடம் மற்றும் வானிலை",
        location_helper: "வானிலை தரவைப் பெற உங்கள் இடம் தேவை.",
        btn_location: "தற்போதைய இடத்தைப் பெறுக",
        btn_predict: "சிறந்த பயிரைக் கணிக்கவும்",
        loading_text: "மண் மற்றும் வானிலை தரவுகளை பகுப்பாய்வு செய்கிறது...",
        results_title: "🤖 AI கணிப்பு முடிவுகள்",
        res_best_crop: "🌾 பயிரிடச் சிறந்த பயிர்",
        res_profitable: "💰 சிறந்த 3 மாற்றுப் பயிர்கள்",
        res_env: "🌦️ சுற்றுச்சூழல் நிலை",
        btn_reset: "மீண்டும் தொடங்குக"
    }
};

document.addEventListener("DOMContentLoaded", () => {
    // Language Switcher Logic
    const langSelect = document.getElementById("language-switcher");
    langSelect.addEventListener("change", (e) => {
        const lang = e.target.value;
        document.querySelectorAll("[data-i18n]").forEach(el => {
            const key = el.getAttribute("data-i18n");
            if (translations[lang] && translations[lang][key]) {
                el.innerHTML = translations[lang][key];
            }
        });
    });


    const form = document.getElementById("agri-form");
    const btnLocation = document.getElementById("btn-location");
    const btnPredict = document.getElementById("btn-predict");
    const locationStatus = document.getElementById("location-status");
    
    const inputLat = document.getElementById("lat");
    const inputLon = document.getElementById("lon");
    
    const loadingSection = document.getElementById("loading");
    const resultsSection = document.getElementById("results");
    const btnReset = document.getElementById("btn-reset");

    // Fetch Location
    btnLocation.addEventListener("click", () => {
        if ("geolocation" in navigator) {
            locationStatus.textContent = "Fetching location...";
            locationStatus.className = "status-msg";
            
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    inputLat.value = position.coords.latitude;
                    inputLon.value = position.coords.longitude;
                    locationStatus.textContent = "Location secured successfully!";
                    locationStatus.className = "status-msg success";
                    btnPredict.disabled = false;
                },
                (error) => {
                    console.error("Error getting location:", error);
                    locationStatus.textContent = "Failed to get location. Please allow location access.";
                    locationStatus.className = "status-msg error";
                    // For demo purposes, we will still allow prediction with dummy coordinates
                    inputLat.value = 20.5937; // Center of India
                    inputLon.value = 78.9629;
                    btnPredict.disabled = false;
                }
            );
        } else {
            locationStatus.textContent = "Geolocation is not supported by your browser.";
            locationStatus.className = "status-msg error";
        }
    });

    // Handle Form Submit
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        if(!inputLat.value || !inputLon.value) {
            alert("Please get your location first.");
            return;
        }

        const payload = {
            soil_answers: {
                color: document.getElementById("soil-color").value,
                texture: document.getElementById("soil-texture").value,
                water_retention: document.getElementById("water-retention").value
            },
            location: {
                lat: parseFloat(inputLat.value),
                lon: parseFloat(inputLon.value)
            }
        };

        // Show loading
        form.classList.add("hidden");
        loadingSection.classList.remove("hidden");

        try {
            // Adjust the URL if deploying remotely.
            const response = await fetch("http://localhost:8000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error("Failed to get prediction from server.");
            }

            const data = await response.json();
            
            displayResults(data);

        } catch (error) {
            console.error(error);
            alert("Error predicting crop. Make sure the backend server is running.");
            loadingSection.classList.add("hidden");
            form.classList.remove("hidden");
        }
    });

    function displayResults(data) {
        loadingSection.classList.add("hidden");
        resultsSection.classList.remove("hidden");

        // Best Crop
        document.getElementById("best-crop").textContent = data.best_crop;

        // Profitable Alternatives
        const profitList = document.getElementById("profitable-crops");
        profitList.innerHTML = "";
        data.top_profitable_crops.forEach((crop, index) => {
            const li = document.createElement("li");
            li.innerHTML = `<span>#${index + 1} ${crop}</span> <span style="color:var(--primary)"><i class="fas fa-arrow-up"></i> High Profit</span>`;
            profitList.appendChild(li);
        });

        // Env Stats
        document.getElementById("res-ph").textContent = data.estimated_soil.pH.toFixed(1);
        document.getElementById("res-npk").textContent = `${data.estimated_soil.N}/${data.estimated_soil.P}/${data.estimated_soil.K}`;
        document.getElementById("res-temp").textContent = `${data.weather.temp.toFixed(1)}°C`;
        document.getElementById("res-hum").textContent = `${data.weather.humidity.toFixed(1)}%`;
    }

    // Reset
    btnReset.addEventListener("click", () => {
        resultsSection.classList.add("hidden");
        form.reset();
        inputLat.value = "";
        inputLon.value = "";
        locationStatus.textContent = "";
        btnPredict.disabled = true;
        form.classList.remove("hidden");
    });
});
