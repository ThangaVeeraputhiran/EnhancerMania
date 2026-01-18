# 🎧 Noise Removal & Speech Enhancement System

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A production-ready web application for noise removal and speech enhancement using advanced deep learning techniques. Perfect for improving audio quality by removing background noise while preserving speech clarity.

## ✨ Features

- **🎯 Advanced Noise Reduction**: Multiple enhancement profiles (Light, Medium, High, Maximum)
- **🎤 Speech Preservation**: Intelligently preserves voice while removing noise
- **📊 Real-time Processing**: Fast audio processing with visual feedback
- **📈 Spectrogram Visualization**: Before/after comparison with spectrograms
- **🌐 Web Interface**: Easy-to-use drag-and-drop interface
- **🔊 Volume Preservation**: Maintains original audio levels
- **📱 Responsive Design**: Works on desktop and mobile devices

## 🚀 Live Demo

Visit the live application: [Your Vercel URL will appear here after deployment]

## 🖼️ Screenshots

Upload your audio file and see instant results with visual spectrogram comparisons!

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Audio Processing**: Librosa, SciPy, NumPy, SoundFile
- **Visualization**: Matplotlib
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Vercel

## 📦 Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/noise_removing_project.git
cd noise_removing_project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app_production.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## 🌐 Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/noise_removing_project)

1. Click the "Deploy with Vercel" button above
2. Or manually deploy:
   - Install Vercel CLI: `npm install -g vercel`
   - Run: `vercel`
   - Follow the prompts

## 📖 Usage

1. **Upload Audio**: Click or drag & drop your audio file (WAV, MP3, FLAC, OGG)
2. **Select Profile**: Choose enhancement level:
   - **Light**: Minimal noise reduction, natural sound
   - **Medium**: Balanced noise reduction
   - **High**: Strong noise reduction
   - **Maximum**: Extreme noise elimination
3. **Process**: Click "Process Audio" and wait for results
4. **Download**: Download the enhanced audio file

## 🎯 Enhancement Profiles

| Profile | Use Case | Processing |
|---------|----------|------------|
| Light | Slight background noise | Gentle spectral subtraction |
| Medium | Moderate noise levels | Balanced multi-stage processing |
| High | Heavy background noise | Advanced Wiener filtering |
| Maximum | Extreme noise conditions | Multi-pass aggressive reduction |

## 📁 Project Structure

```
noise_removing_project/
├── app_production.py          # Main Flask application
├── production_system.py       # Core audio processing system
├── extreme_noise_eliminator.py # Advanced noise reduction
├── enhanced_speech_processor.py # Speech enhancement
├── ultra_speech_enhancer.py   # Ultra-quality processing
├── templates/                 # HTML templates
├── static/                    # CSS, JS, and images
├── uploads/                   # Temporary upload storage
├── outputs/                   # Processed audio files
└── requirements.txt           # Python dependencies
```

## 🔧 Configuration

Key parameters can be adjusted in `config_params.py`:
- Sample rate
- Frame size
- Noise reduction thresholds
- Enhancement profiles

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Your Name** - Initial work

## 🙏 Acknowledgments

- TIMIT dataset for clean voice samples
- AudioSet for noise classification
- Flask framework for web interface
- Librosa for audio processing

## 📞 Contact

For questions or feedback, please open an issue on GitHub.

---

⭐ If you find this project useful, please consider giving it a star!
