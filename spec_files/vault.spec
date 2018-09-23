%undefine _disable_source_fetch
%define debug_package %{nil}
Name:           vault
Version:        jeff
Release:        11.1
Summary:        vault secret storage

Group:          nomad_cloud
BuildArch:      x86_64
License:        MPL2
URL:            https://www.vaultproject.io/
Source0:        https://releases.hashicorp.com/vault/0.11.1/vault_0.11.1_linux_amd64.zip
Source1:        https://github.com/jeffreyhodge/cloud/raw/master/systemd/vault.service


%description
Secrets storage

%prep
%setup -q -c -n builddir
%build
%install
cp %{_sourcedir}/vault.service %{_builddir}/builddir
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/sbin
install -m 0755 vault $RPM_BUILD_ROOT/usr/local/sbin/vault
install -m 0755 -d $RPM_BUILD_ROOT/etc/vault.d
install -m 0755 -d $RPM_BUILD_ROOT/etc/systemd/system
install -m 0644 vault.service $RPM_BUILD_ROOT/etc/systemd/system/vault.service

%files
/usr/local/sbin/vault
/etc/vault.d
/etc/systemd/system/vault.service

%pre
getent group vault >/dev/null || groupadd -r vault
getent passwd vault >/dev/null || \
    useradd -r -g vault -d /home/vault -s /sbin/nologin \
    -c "Vault user" vault
exit 0

%changelog
